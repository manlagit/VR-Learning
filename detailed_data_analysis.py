import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from scipy import stats

class DetailedDataAnalysis:
    def __init__(self, csv_file):
        """Initialize with CSV file path."""
        self.data = pd.read_csv(csv_file)
        self.setup_database()

    def setup_database(self):
        """Step 1: Set up SQLite database."""
        conn = sqlite3.connect('sign_language.db')
        self.data.to_sql('student_data', conn, if_exists='replace', index=False)
        conn.close()

    def calculate_learning_gains(self):
        """Step 2: Calculate learning gains."""
        print("\n" + "="*80)
        print("STEP 2: CALCULATE LEARNING GAINS")
        print("="*80)
        
        self.data['Vocabulary_Gain'] = self.data['Post_Sign_Vocabulary_Score'] - self.data['Pre_Sign_Vocabulary_Score']
        self.data['Comprehension_Gain'] = self.data['Post_Comprehension_Score'] - self.data['Pre_Comprehension_Score']
        self.data['Production_Gain'] = self.data['Post_Production_Score'] - self.data['Pre_Production_Score']
        
        conn = sqlite3.connect('sign_language.db')
        self.data.to_sql('student_data', conn, if_exists='replace', index=False)
        conn.close()
        
        print("✓ Learning gains calculated and saved to database")

    def perform_descriptive_statistics(self):
        """Step 3: Perform descriptive statistics."""
        print("\n" + "="*80)
        print("STEP 3: DESCRIPTIVE STATISTICS")
        print("="*80)
        
        stats_summary = self.data.describe()
        print(stats_summary)
        
        conn = sqlite3.connect('sign_language.db')
        stats_summary.to_sql('descriptive_stats', conn, if_exists='replace')
        conn.close()
        
        print("✓ Descriptive statistics calculated and saved to database")

    def perform_inferential_statistics(self):
        """Step 4: Perform inferential statistics."""
        print("\n" + "="*80)
        print("STEP 4: INFERENTIAL STATISTICS")
        print("="*80)
        
        t_tests = {}
        effect_sizes = {}
        assessments = {
            'Vocabulary': ('Pre_Sign_Vocabulary_Score', 'Post_Sign_Vocabulary_Score'),
            'Comprehension': ('Pre_Comprehension_Score', 'Post_Comprehension_Score'),
            'Production': ('Pre_Production_Score', 'Post_Production_Score')
        }
        
        for assessment, (pre_col, post_col) in assessments.items():
            t_stat, p_val = stats.ttest_rel(self.data[pre_col], self.data[post_col])
            t_tests[assessment] = {'t-statistic': t_stat, 'p-value': p_val}
            effect_size = (self.data[post_col].mean() - self.data[pre_col].mean()) / self.data[pre_col].std()
            effect_sizes[assessment] = effect_size
        
        print("T-test Results:", t_tests)
        print("Effect Sizes (Cohen's d):", effect_sizes)
        
        conn = sqlite3.connect('sign_language.db')
        pd.DataFrame(t_tests).T.to_sql('t_test_results', conn, if_exists='replace')
        pd.DataFrame(effect_sizes, index=['Cohen\'s d']).to_sql('effect_sizes', conn, if_exists='replace')
        conn.close()
        
        print("✓ Inferential statistics calculated and saved to database")

def perform_subgroup_analysis(self):
    """Step 5: Perform subgroup analysis."""
    print("\n" + "="*80)
    print("STEP 5: SUBGROUP ANALYSIS")
    print("="*80)
    
    gender_gains = self.data.groupby('Gender')[['Vocabulary_Gain', 'Comprehension_Gain', 'Production_Gain']].mean()
    grade_gains = self.data.groupby('Grade_Level')[['Vocabulary_Gain', 'Comprehension_Gain', 'Production_Gain']].mean()
    
    # Corrected line: observed=True moved to groupby()
    age_bins = pd.cut(self.data['Age'], bins=range(6, 14))
    age_gains = self.data.groupby(age_bins, observed=True)[['Vocabulary_Gain', 'Comprehension_Gain', 'Production_Gain']].mean()
    
    print("Gender Gains:\n", gender_gains)
    print("Grade Level Gains:\n", grade_gains)
    print("Age Group Gains:\n", age_gains)
    
    conn = sqlite3.connect('sign_language.db')
    gender_gains.to_sql('gender_gains', conn, if_exists='replace')
    grade_gains.to_sql('grade_gains', conn, if_exists='replace')
    age_gains.to_sql('age_gains', conn, if_exists='replace')
    conn.close()
    
    print("✓ Subgroup analysis completed and saved to database")
    
    def perform_qualitative_analysis(self):
        """Step 6: Perform qualitative analysis (placeholder)."""
        print("\n" + "="*80)
        print("STEP 6: QUALITATIVE ANALYSIS")
        print("="*80)
        print("✓ Qualitative analysis completed (placeholder implementation)")
        # Placeholder for actual qualitative analysis from JSON files

    def integrate_findings(self):
        """Step 7: Integrate quantitative and qualitative findings."""
        print("\n" + "="*80)
        print("STEP 7: INTEGRATE FINDINGS")
        print("="*80)
        print("✓ Findings integrated (placeholder implementation)")
        # Placeholder for integration logic

    def create_comprehensive_visualizations(self):
        """Step 8: Enhanced Visualization"""
        print("\n" + "="*80)
        print("STEP 8: COMPREHENSIVE VISUALIZATIONS")
        print("="*80)
        
        # Set up the plotting style
        plt.style.use('default')
        sns.set_palette("husl")
        
        # 1. Pre-test vs Post-test Comparison (Box plots)
        fig1 = plt.figure(figsize=(8, 6))
        ax1 = plt.subplot()
        pre_post_data = []
        labels = []
        assessment_mapping = {
            'Vocabulary': ('Pre_Sign_Vocabulary_Score', 'Post_Sign_Vocabulary_Score'),
            'Comprehension': ('Pre_Comprehension_Score', 'Post_Comprehension_Score'),
            'Production': ('Pre_Production_Score', 'Post_Production_Score')
        }
        for assessment, (pre_col, post_col) in assessment_mapping.items():
            pre_post_data.extend([self.data[pre_col], self.data[post_col]])
            labels.extend([f'Pre-{assessment}', f'Post-{assessment}'])
        bp = ax1.boxplot(pre_post_data, labels=labels, patch_artist=True)
        colors = ['lightblue', 'lightgreen'] * 3
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
        ax1.set_title('Pre-test vs Post-test Score Distributions', fontsize=16)
        ax1.set_ylabel('Score', fontsize=14)
        ax1.set_xlabel('Assessment Type', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('fig_pre_post_scores.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 2. Learning Gains by Assessment Type
        fig2 = plt.figure(figsize=(8, 6))
        ax2 = plt.subplot()
        gains = [self.data['Vocabulary_Gain'].mean(), self.data['Comprehension_Gain'].mean(), self.data['Production_Gain'].mean()]
        gain_std = [self.data['Vocabulary_Gain'].std(), self.data['Comprehension_Gain'].std(), self.data['Production_Gain'].std()]
        bars = ax2.bar(['Vocabulary', 'Comprehension', 'Production'], gains, yerr=gain_std, capsize=5, alpha=0.8, color=['skyblue', 'lightgreen', 'lightcoral'])
        ax2.set_title('Average Learning Gains with Error Bars', fontsize=16)
        ax2.set_ylabel('Learning Gain (Points)', fontsize=14)
        ax2.set_xlabel('Assessment Type', fontsize=14)
        for bar, gain in zip(bars, gains):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 1, f'{gain:.1f}', ha='center', va='bottom', fontsize=12)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('fig_learning_gains.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 3. VR Reaction Scores
        fig3 = plt.figure(figsize=(8, 6))
        ax3 = plt.subplot()
        vr_metrics = ['Satisfaction', 'Ease of Use', 'Engagement', 'Recommendation']
        vr_scores = [self.data['VR_Satisfaction_Overall'].mean(), self.data['VR_Ease_of_Use'].mean(), self.data['VR_Engagement_Level'].mean(), self.data['VR_Recommendation'].mean()]
        bars = ax3.bar(vr_metrics, vr_scores, color=['skyblue', 'lightgreen', 'lightcoral', 'orange'], alpha=0.8)
        ax3.set_title('VR Application Reaction Scores', fontsize=16)
        ax3.set_ylabel('Average Rating (1-5)', fontsize=14)
        ax3.set_xlabel('Metric', fontsize=14)
        ax3.set_ylim(0, 5)
        ax3.axhline(y=4, color='red', linestyle='--', alpha=0.7, label='Target = 4.0')
        for bar, score in zip(bars, vr_scores):
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height + 0.05, f'{score:.2f}', ha='center', va='bottom', fontsize=12)
        plt.xticks(fontsize=12)
        plt.legend()
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('fig_vr_reaction_scores.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 4. Demographics - Age Distribution
        fig4 = plt.figure(figsize=(8, 6))
        ax4 = plt.subplot()
        ax4.hist(self.data['Age'], bins=range(6, 14), alpha=0.7, color='skyblue', edgecolor='black')
        ax4.set_title('Age Distribution (N=100)', fontsize=16)
        ax4.set_xlabel('Age (Years)', fontsize=14)
        ax4.set_ylabel('Number of Students', fontsize=14)
        plt.xticks(fontsize=12)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('fig_age_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 5. Demographics - Gender Distribution
        fig5 = plt.figure(figsize=(6, 6))
        ax5 = plt.subplot()
        gender_counts = self.data['Gender'].value_counts()
        ax5.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12}, colors=['blue', 'orange', 'green'])
        ax5.set_title('Gender Distribution', fontsize=16)
        plt.tight_layout()
        plt.savefig('fig_gender_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 6. Learning Gains Distribution
        fig6 = plt.figure(figsize=(8, 6))
        ax6 = plt.subplot()
        ax6.hist([self.data['Vocabulary_Gain'], self.data['Comprehension_Gain'], self.data['Production_Gain']], bins=15, alpha=0.7, label=['Vocabulary', 'Comprehension', 'Production'], color=['pink', 'gold', 'lightgreen'])
        ax6.set_title('Learning Gains Distribution', fontsize=16)
        ax6.set_xlabel('Learning Gain (Points)', fontsize=14)
        ax6.set_ylabel('Frequency', fontsize=14)
        ax6.legend(fontsize=12)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('fig_learning_gains_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 7. Satisfaction vs Vocabulary Gain Scatter
        fig7 = plt.figure(figsize=(8, 6))
        ax7 = plt.subplot()
        scatter = ax7.scatter(self.data['VR_Satisfaction_Overall'], self.data['Vocabulary_Gain'], alpha=0.6, c=self.data['Age'], cmap='viridis')
        ax7.set_xlabel('VR Satisfaction Rating', fontsize=14)
        ax7.set_ylabel('Vocabulary Learning Gain', fontsize=14)
        ax7.set_title('Satisfaction vs Vocabulary Gains (colored by age)', fontsize=16)
        plt.colorbar(scatter, ax=ax7, label='Age', orientation='vertical')
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('fig_satisfaction_vs_vocab_gain.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 8. Grade Level vs Average Gains
        fig8 = plt.figure(figsize=(10, 6))
        ax8 = plt.subplot()
        grade_gains = self.data.groupby('Grade_Level')[['Vocabulary_Gain', 'Comprehension_Gain', 'Production_Gain']].mean()
        grade_gains.plot(kind='bar', ax=ax8, alpha=0.8, color=['blue', 'orange', 'green'])
        ax8.set_title('Average Learning Gains by Grade Level', fontsize=16)
        ax8.set_xlabel('Grade Level', fontsize=14)
        ax8.set_ylabel('Average Gain (Points)', fontsize=14)
        ax8.legend(title='Assessment Type', fontsize=12)
        plt.xticks(rotation=0, fontsize=12)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('fig_grade_level_gains.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 9. Success Metrics Dashboard
        fig9 = plt.figure(figsize=(10, 6))
        ax9 = plt.subplot()
        positive_exp = (self.data['VR_Satisfaction_Overall'] >= 4).mean() * 100
        high_engagement = (self.data['VR_Engagement_Level'] >= 4).mean() * 100
        recommend = (self.data['VR_Recommendation'] >= 4).mean() * 100
        skill_improvement = (self.data['Vocabulary_Gain'] >= 10).mean() * 100
        metrics = ['Positive\nExperience\n(≥80%)', 'High\nEngagement\n(≥75%)', 'Recommend\n(≥70%)', 'Skill\nImprovement\n(≥60%)']
        values = [positive_exp, high_engagement, recommend, skill_improvement]
        targets = [80, 75, 70, 60]
        bars = ax9.bar(metrics, values, alpha=0.8, color=['skyblue', 'lightgreen', 'lightcoral', 'orange'])
        for i, (bar, value, target) in enumerate(zip(bars, values, targets)):
            if value >= target:
                bar.set_color('green')
            else:
                bar.set_color('red')
        ax9.set_ylabel('Percentage (%)', fontsize=14)
        ax9.set_title('Success Metrics Achievement', fontsize=16)
        ax9.set_xlabel('Metrics', fontsize=14)
        ax9.set_ylim(0, 100)
        for i, target in enumerate(targets):
            ax9.axhline(y=target, color='black', linestyle='--', alpha=0.5)
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('fig_success_metrics.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 10. Correlation Heatmap
        fig10 = plt.figure(figsize=(8, 6))
        ax10 = plt.subplot()
        corr_vars = ['Age', 'Vocabulary_Gain', 'Comprehension_Gain', 'Production_Gain', 'VR_Satisfaction_Overall', 'VR_Ease_of_Use', 'VR_Engagement_Level', 'VR_Recommendation']
        corr_matrix = self.data[corr_vars].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, square=True, ax=ax10, cbar_kws={'shrink': 0.8}, annot_kws={'size': 12})
        ax10.set_title('Correlation Matrix', fontsize=16)
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        plt.savefig('fig_correlation_matrix.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 11. Learning Gains by Gender
        fig11 = plt.figure(figsize=(8, 6))
        ax11 = plt.subplot()
        gender_gains = self.data.groupby('Gender')[['Vocabulary_Gain', 'Comprehension_Gain', 'Production_Gain']].mean()
        gender_gains.plot(kind='bar', ax=ax11, alpha=0.8, color=['blue', 'orange', 'green'])
        ax11.set_title('Learning Gains by Gender', fontsize=16)
        ax11.set_xlabel('Gender', fontsize=14)
        ax11.set_ylabel('Average Gain (Points)', fontsize=14)
        ax11.legend(title='Assessment Type', fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=0, fontsize=12)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('fig_learning_gains_by_gender.png', dpi=300, bbox_inches='tight')
        plt.close()

        # 12. VR Satisfaction Distribution
        fig12 = plt.figure(figsize=(8, 6))
        ax12 = plt.subplot()
        satisfaction_counts = self.data['VR_Satisfaction_Overall'].value_counts().sort_index()
        ax12.bar(satisfaction_counts.index, satisfaction_counts.values, alpha=0.8, color='skyblue')
        ax12.set_title('VR Satisfaction Rating Distribution', fontsize=16)
        ax12.set_xlabel('Satisfaction Rating (1-5)', fontsize=14)
        ax12.set_ylabel('Number of Students', fontsize=14)
        for rating, count in satisfaction_counts.items():
            percentage = (count / len(self.data)) * 100
            ax12.text(rating, count + 1, f'{percentage:.1f}%', ha='center', va='bottom', fontsize=12)
        plt.xticks(fontsize=12)
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.savefig('fig_vr_satisfaction_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("✓ Individual visualizations saved as separate PNG files")

    def run_complete_analysis(self):
        """Run the complete analysis pipeline."""
        self.calculate_learning_gains()
        self.perform_descriptive_statistics()
        self.perform_inferential_statistics()
        self.perform_subgroup_analysis()
        self.perform_qualitative_analysis()
        self.integrate_findings()
        self.create_comprehensive_visualizations()

if __name__ == "__main__":
    analyzer = DetailedDataAnalysis('student_data.csv')
    analyzer.run_complete_analysis()